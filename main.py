import argparse
import sys
import os
from datetime import date, datetime
from sendText import sendText
import time


def parse_args():
  """
  Parse input arguments
  """
  parser = argparse.ArgumentParser(description='employee Name')
  parser.add_argument('--phone',
                         help='enter phone number',
                        type=str)
  parser.add_argument('--name', help='name',
                      type=str)
  parser.add_argument('--msg', help='Message',
                      type=str)
  parser.add_argument('--carrier', help='Carrier',
                    type=str)                    
  parser.add_argument('--waitTime', help='wait time',
                  type=int)  
  args = parser.parse_args()
  return args

if __name__ == '__main__':
    # workdir = os.path.dirname(__file__)
    # os.chdir(workdir)
    args = parse_args()
    print("sending text for {}".format(args.name))
    # today = date.today().strftime("%m/%d/%Y")

    msg = args.msg + "\n"
    carrier = args.carrier
    phone = args.phone
    name = args.name

    sendText("Texting Program\n", msg, phone, carrier)
    sys.exit("Label printed")