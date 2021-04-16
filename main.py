# #grakn
from grakn.client import *
import pre_process

help_list = pre_process.pre_process(direct = r"C:\Users\kunge\Downloads\AIEngineer\AIEngineer\gtc_AI.engineer_Projektbeschreibung\DEP_tables2")

with Grakn.core_client("localhost:1729") as client:
    with client.session("hackathon", SessionType.DATA) as session:
        
# # feed data into database
#         with session.transaction(TransactionType.WRITE) as transaction:
#             for item in help_list:
#                 print("Executing Graql Query: " + str(item))
#                 transaction.query().insert(item)
#             transaction.commit()
