
Connect to a Neon Postgres DB on Cloudflare Workers using pgwasm in Python.

For local dev:

```
echo '
DB_URL=wss://my-db.my-region.aws.neon.tech/v2
DB_DATABASE=mydb
DB_USER=me
DB_PASSWORD=************
' > .dev.vars

npx wrangler@latest dev
```

For deploy (currently not working):

```
npx wrangler@latest secret put DB_URL
# wss://my-db.my-region.aws.neon.tech/v2

npx wrangler@latest secret put DB_DATABASE
# mydb

npx wrangler@latest secret put DB_USER
# me

npx wrangler@latest secret put DB_PASSWORD
# ************

npx wrangler@latest dev
```
