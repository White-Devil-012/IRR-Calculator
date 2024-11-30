from flask import Flask, request, render_template
import numpy_financial as npf

app = Flask(__name__)

def calculate_irr(cash_outflow, time, cash_inflow):
    cash_flows = [cash_outflow] * time + [cash_inflow]
    irr = npf.irr(cash_flows)
    return irr * 100

@app.route("/", methods=["GET", "POST"])
def irr_calculator():
    if request.method == "POST":
        try:
            # Get input values from the form
            cash_outflow = float(request.form["cash_outflow"])
            time = int(request.form["time"])
            cash_inflow = float(request.form["cash_inflow"])

            # Validate inputs
            if cash_outflow >= 0 or time <= 0 or cash_inflow <= 0:
                return render_template("index.html", error="Invalid input! Check the values and try again.")
            
            # Calculate IRR
            irr_result = calculate_irr(cash_outflow, time, cash_inflow)
            return render_template("index.html", result=f"The IRR is {irr_result:.2f}%")
        except ValueError:
            return render_template("index.html", error="Invalid input! Please enter valid numeric values.")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
