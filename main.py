import requests

def main():
    
    generate_webhook_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

    payload = {
        "name": "Shrey Parikh",
        "regNo": "0827AL221123", 
        "email": "shreymait220543@acropolis.in"
    }

    response = requests.post(generate_webhook_url, json=payload)
    response_data = response.json()

    webhook_url = response_data.get('webhook')
    access_token = response_data.get('accessToken')

    
    final_query = """
    SELECT 
        p.amount AS SALARY,
        CONCAT(e.first_name, ' ', e.last_name) AS NAME,
        FLOOR(DATEDIFF(CURRENT_DATE, e.dob) / 365.25) AS AGE,
        d.department_name AS DEPARTMENT_NAME
    FROM 
        payments p
    JOIN 
        employee e ON p.emp_id = e.emp_id
    JOIN 
        department d ON e.department = d.department_id
    WHERE 
        DAY(p.payment_time) != 1
    ORDER BY 
        p.amount DESC
    LIMIT 1;
    """

    
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    submission_payload = {
        "finalQuery": final_query.strip()
    }

    submission_response = requests.post(webhook_url, headers=headers, json=submission_payload)

    print("Submission Status Code:", submission_response.status_code)
    print("Submission Response Body:", submission_response.text)

if __name__ == "__main__":
    main()
