import requests
import json

def get_azure_instance_metadata(key=None):
    # Define the Azure metadata URL
    metadata_url = "http://<instance-IP>/metadata/instance"
    headers = {"Metadata": "true"}  # Required header for Azure Metadata Service

    try:
        # Make a GET request to the metadata service
        response = requests.get(metadata_url, headers=headers, params={"api-version": "2021-02-01"})
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response as JSON
        metadata = response.json()

        # If no specific key is provided, return the full metadata
        if key is None:
            print(json.dumps(metadata, indent=4))
            return metadata
        else:
            # Retrieve a specific key from the metadata if it exists
            value = metadata.get(key, "Key not found in metadata")
            print(json.dumps({key: value}, indent=4))
            return {key: value}

    except requests.exceptions.RequestException as e:
        print(f"Error querying Azure metadata: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    # To get the full metadata
    get_azure_instance_metadata()

    # To get a specific key (for example, 'compute')
    get_azure_instance_metadata("compute")
