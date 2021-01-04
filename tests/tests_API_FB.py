# Import and load necessary lib
# import sys
# sys.path.append('vagrant\ultimatejob')
import API_FB


# Test functions
def test_api_urls():
    """The testing will check if our functions return the required output"""
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_FB.create_soup(API_FB.create_req())
    expected_output_urls = ['https://www.facebook.com/careers/v2/jobs/1672813472870915/',
                            'https://www.facebook.com/careers/v2/jobs/712878282607325/',
                            'https://www.facebook.com/careers/v2/jobs/420212419368641/',
                            'https://www.facebook.com/careers/v2/jobs/207984144060781/',
                            'https://www.facebook.com/careers/v2/jobs/773785633436218/',
                            'https://www.facebook.com/careers/v2/jobs/2597607417128369/',
                            'https://www.facebook.com/careers/v2/jobs/536078547072736/']
    assert API_FB.extract_jobs_url(soup) == expected_output_urls, "The tests for URLs were successful"


def test_api_titles():
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_FB.create_soup(API_FB.create_req())
    """The testing will check if our functions return the required output"""
    expected_output_titles = ['Production Engineer', 'Offensive Security Engineer Intern, Red Team',
                              'Internal Audit Manager – Infrastructure', 'Production Engineer',
                              'Production Engineer', 'Production Engineer', 'Production Engineer']
    assert API_FB.extract_jobs_title(soup) == expected_output_titles, "The tests for URLs were successful"