{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b4ca9ef3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import Flask and jsonify\n",
    "from flask import Flask, jsonify, request\n",
    "# import Resource, Api and reqparser\n",
    "from flask_restful import Resource, Api, reqparse\n",
    "import pandas as pd\n",
    "import numpy\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "47a74466",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "api = Api(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "41ca3b64",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = pickle.load( open( \"model1.p\", \"rb\" ) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "789f2ebe",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Scoring(Resource):\n",
    "    def post(self):\n",
    "        json_data = request.get_json()\n",
    "        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()\n",
    "        # getting predictions from our model.\n",
    "        # it is much simpler because we used pipelines during development\n",
    "        res = model.predict_proba(df)\n",
    "        # we cannot send numpt array as a result\n",
    "        return res.tolist() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c3330163",
   "metadata": {},
   "outputs": [],
   "source": [
    "# assign endpoint\n",
    "api.add_resource(Scoring, '/scoring')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c04bf297",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with windowsapi reloader\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Matthew Wong\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3445: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f24ce95d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
