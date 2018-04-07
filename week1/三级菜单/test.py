#/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Auther:yooma 2016-08-14 22:00
import sys
execLaye = {1:{"北京":{1:{"东城":{1:{"建国门":{1:"建国门大厦",2:"门建国大厦"}},2:{"东单":{1:"东单大厦",2:"单东大厦"}}}
                         },
                       2:{"西城":{1:{"阜成门":{1:"四川大厦",2:"中基大厦"}},2:{"西直门":{1:"沸腾鱼",2:"西直门桥"}}}
                         },
                      }
              },
            2:{"上海":{1:{"浦东":{1:{"浦东一":{1:"浦东一大厦",2:"浦东一一大厦"}},2:{"浦东二":{1:"浦东二大厦",2:"浦东二二大厦"}}}
                         },
                       2:{"东环":{1:{"东环一":{1:"东环一大厦",2:"东环一一大厦"}},2:{"东环二":{1:"东环二大厦",2:"东环二二大厦"}}}
                         }
                      },
              },
           }
def help():
    print('''
          Useage:
                 1. [ h ]  -- help to useaga.
                 2. [ 1 | 2 ] -- Input city number selected [1 or 2] into it.
                 3. [ b ]  -- "b" parameter function is to return to the previous level menu.
                 4. [ q | quit | exit ] -- function is exit current program.
          ''')
def select(value, record):
    city = ""
    for k, v in value.items():
        if isinstance(v,str):
            city = city + '\t' + str(k) + '.' + ' %s\n' % v
        else:
            city = city + '\t' + str(k) + '.' + ' %s\n' % list(v.keys())[0]
#    SelectCity = input("%sSelect please: " % city)
    while 1:
        SelectCity = input("%sSelect please: " % city)
        if SelectCity == 'h':
            help()
        #    sys.exit(0)
        for n, i in value.items():
            if SelectCity == str(n):
                if isinstance(i,str):
                    print("~~~~~~~Welcome to %s ~~~~~~~" % i)
                    sys.exit(0)
                else:
                    print("[ Welcome to %s ]" % list(i.keys())[0])
                    select(list(i.values())[0], value)
            elif SelectCity == 'b':
                select(record, record)
            elif SelectCity == 'q' or SelectCity == 'quit' or SelectCity == 'exit':
                sys.exit(0)
            else:
                continue
if __name__ == "__main__":
    select(execLaye,execLaye)