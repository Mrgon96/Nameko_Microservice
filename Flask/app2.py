from flask import Flask, request
from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy

app=Flask(__name__)
Swagger(app)
CONFIG={'AMQP_URI': "amqp://guest:guest@localhost"}


@app.route('/sender', methods=['POST'])
def sender():
    """
    Micro Service Based Compute and Mail API
    This API is made with Flask, Flasgger and Nameko
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          properties:
            email:
              type: string
    responses:
      200:
        description: Email is Sent
    """

    email = request.json.get('email')
    msg = "API for Nameko"
    subject = "Nameko Send Mail Microservice"
    with ClusterRpcProxy as rpc:
        rpc.send_mail.send.async(email, subject, msg)
        return "Email Sent", 200


if __name__ == '__main__':
    app.run(debug=False)
