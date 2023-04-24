user = {'aeinstein':{'first':'albert',
                     'last':'aeinstein',
                     'location':'princeton'
                    },
        'mcuire':{'first':'marie',
                  'last':'curie',
                  'location':'paris'
                },
        }

for user,user_info in user.items():
    print(f"Username: {user.title()}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")