from pritunl_api import *
import pprint
pprint.pprint(json)
pri = Pritunl(url="https://yoursite.com",
            token="###",
            secret="###")

# delete user
org_id = ""
users = pri.user.get(org_id=org_id)
email_delete = "quyet@abc.com"
for user in users:
    if user["name"] == email_delete:
        pri.user.delete(org_id=user["organization"], usr_id=user["id"])


print(pri.ping())
# view org 
q = pri.user.get(org_id="")
# View users id
q = pri.user.get(org_id=x[0]['id'])
# Delete users
pri.user.delete(org_id=x[0]['id'], user_id=q[1]['id'])

print(q)
