from indeed import extract_indeed_pages, extract_indeed_jobs

indeed_max_pages = extract_indeed_pages()

extract_indeed_jobs(indeed_max_pages + 1)