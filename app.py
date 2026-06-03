from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/saveLead', methods=['POST'])
def save_lead():

    data = request.json

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",   # your MySQL password
        database="zaillor_db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leads
        (lead_id, website_url, email, phone, created_at,
         overall_score, lead_status)
        VALUES (%s,%s,%s,%s,NOW(),%s,%s)
    """, (
        data["leadId"],
        data["websiteUrl"],
        data["email"],
        data["phone"],
        data["overallScore"],
        data["leadStatus"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"success": True})

print("Flask reached bottom")

if __name__ == "__main__":
    app.run(debug=True)