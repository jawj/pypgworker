# enable imports from local `lib` folder
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent / "lib"))

import js
import json
import pgwasm.dbapi

async def on_fetch(request, env):
    # connect and run SQL query
    conn = await pgwasm.dbapi.connect(uri=env.DB_URI, user=env.DB_USER, password=env.DB_PASSWORD, database=env.DB_DATABASE)
    curs = conn.cursor()
    await curs.execute("SELECT * FROM employees")
    rows = curs.fetchall()
    conn.close()

    # process results into JSON object
    keys = [k[0] for k in curs.description]
    results = [dict(zip(keys, row)) for row in rows]
    jsonres = json.dumps(results, default=str)

    # respond
    headers = js.Headers.new({"content-type": "application/json"}.items())
    return js.Response.new(jsonres, headers=headers)
