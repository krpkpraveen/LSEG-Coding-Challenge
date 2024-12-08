# LSEG-Coding-Challenge
LSEG: Pre-Interview Coding Challenge

Summary:
    Here’s a Python script that queries the metadata of an instance within Azure/AWS and outputs the data in JSON format.
    Azure provides metadata about an instance through a well-defined metadata service available at http://<instance-IP>/metadata/instance.

Key Points:
    Metadata API URL:
        The metadata service is accessed at http://<instance-IP>/metadata/instance.
        You must include the Metadata: true header in your request.
    Query Parameters:
        You can specify the api-version parameter to ensure compatibility with the API.
    JSON Formatting:
        The script formats the output using Python's json.dumps function for readability.
    Dependencies:
        Install the requests library if not already available. Use pip install requests.
    Running the Script:
        This script is intended to be run within an Azure VM or environment with access to the metadata endpoint.

Bonus Points : The code allows for a particular data key to be retrieved individually
Summary: So that a specific data key from the Azure instance metadata can be retrieved individually, I can add functionality to allow the user to query a specific key.

key Parameter:
  The function get_azure_instance_metadata now accepts an optional parameter key which allows you to query a specific piece of metadata.
  If the key is provided, it retrieves the corresponding value for that key.
  If the key does not exist, it returns "Key not found in metadata".

Example Usage:
  To retrieve the full metadata, simply call get_azure_instance_metadata().
  To retrieve metadata for a specific key (like compute), call get_azure_instance_metadata("compute").

Example Outputs:
![image](https://github.com/user-attachments/assets/71c1fe89-62d9-42b9-8737-56d536af2687)

Specific Key ("compute"):
![image](https://github.com/user-attachments/assets/8ca73e39-99a1-4fac-9706-65e872a9c173)


