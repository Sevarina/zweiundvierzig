#grakn

from grakn.client import *

with Grakn.core_client("localhost:1729") as client:
    with client.session("social_network", SessionType.DATA) as session:
        ## session is open
        pass
    ## session is closed
## client is closed