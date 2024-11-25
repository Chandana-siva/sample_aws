{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "03b9968f-68d3-4350-889e-ad919895bc57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:1234\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [25/Nov/2024 14:58:21] \"POST /ab HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask,request\n",
    "app=Flask(__name__)\n",
    "@app.route(\"/ab\",methods=[\"POST\"])\n",
    "def ch():\n",
    "    a=int(request.form.get(\"a\"))\n",
    "    b=int(request.form.get(\"b\"))\n",
    "    c=a+b\n",
    "    return str(c)\n",
    "if __name__==\"__main__\":\n",
    "    app.run(port=1234)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ed20c79-b280-413b-a72a-04e4b52ae7b4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
