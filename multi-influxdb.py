from influxdb import InfluxDBClient

client = InfluxDBClient('localhost',8086,'root','root')
client.switch_database('home_db')
# client.write_points([
#         {
#             'measurement': 'temperature',
#             'tags': {
#                 'location': 'lightroom'
#             },
#             'fields': {
#                 'value': 2.0
#             }
#         }
#     ]
# )
# print(client.get_list_database())

client.drop_database('home_db')