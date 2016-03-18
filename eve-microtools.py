from flask import Flask
from flask import request

import pickle
import json

app = Flask(__name__)
#app.debug = True


@app.route('/test/', methods=['GET'])
def test():
    return (
        'Working.',
        200,
        {'Content-Type': 'text/text'}
    )


@app.route('/api/nameToID', methods=['GET'])
def name_to_id():
    names = request.args.get('names')
    if not names:
        return '[]'

    out = []

    with open('invTypes.pyobj', 'rb') as f:
        invTypes = pickle.load(f)
        for name in names.split('|'):
            v = invTypes.get(name, None)
            if v is not None:
                out.append({
                    'typeName': name,
                    'typeID': v
                })

    return (
        json.dumps(out),
        200,
        {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    )

if __name__ == '__main__':
    app.run()
