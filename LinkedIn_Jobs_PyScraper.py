#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import date
current_date = date.today()


# In[ ]:


from linkedin_jobs_pyscraper.models.search.searcher import Searcher
from linkedin_jobs_pyscraper.models.filters import filters
from linkedin_jobs_pyscraper.linkedin_jobs_scraper import LinkedInJobsPyScraper

## create searach query with configurations
searcher = Searcher(
    search_pages_per_search_term = 8,
    search_terms = ['data analyst', 'data scientist','business analytics', 'data analytics'],
    batch_size = 5,
    output_filepath = f'job_search_{current_date}_full_time.csv',
    location = 'Germany'
    )

search_filter = filters.Filters(
    experience= filters.ExperienceLevelFilters.ENTRY_LEVEL,
    job_type= filters.TypeFilters.FULL_TIME,
    relevance= filters.RelevanceFilters.RECENT,
    time= filters.TimeFilters.MONTH
    )
scraper = LinkedInJobsPyScraper(searcher= searcher, filters=search_filter) 
scraper.start()


# In[ ]:


help(searcher)

