# Import the pyshorteners module
import pyshorteners

# Get the URL from the user
url = input("Enter the URL: ")

# Function to shorten the given URL
def shortenurl(url):
    # Create an instance of the Shortener class from pyshorteners
    s = pyshorteners.Shortener()

    # Shorten the URL using the TinyURL service
    short_url = s.tinyurl.short(url)

    # Print the shortened URL
    print("Your shortened link is:", short_url)

# Call the shortenurl function with the user-provided URL
shortenurl(url)
