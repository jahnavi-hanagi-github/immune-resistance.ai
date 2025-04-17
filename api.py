from flask import Flask, jsonify, request
import numpy as np
from scipy.integrate import odeint

app = Flask(__name__)

# SIR model differential equations
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

@app.route('/simulate', methods=['GET'])
def simulate_immune_response():
    # Parameters from query string or default values
    beta = float(request.args.get('beta', 0.3))
    gamma = float(request.args.get('gamma', 0.1))
    S0 = float(request.args.get('S0', 0.99))
    I0 = float(request.args.get('I0', 0.01))
    R0 = float(request.args.get('R0', 0.0))
    days = int(request.args.get('days', 160))

    # Initial conditions vector
    y0 = S0, I0, R0
    t = np.linspace(0, days, days)

    # Solve SIR model
    result = odeint(sir_model, y0, t, args=(beta, gamma))
    S, I, R = result.T

    # Convert to list for JSON serialization
    data = {
        "time": t.tolist(),
        "susceptible": S.tolist(),
        "infected": I.tolist(),
        "recovered": R.tolist()
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

