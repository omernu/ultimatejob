# Import and load necessary lib
import API_FB


def main():
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_FB.create_soup(API_FB.create_req())

    # Return list contains URLs
    API_FB.extract_jobs_url(soup)

    # Return list contains job titles
    API_FB.extract_jobs_title(soup)
