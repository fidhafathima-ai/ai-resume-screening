print("AI Resume Screening System")
print("Project by Fidha Fathima")

# Sample skills matching logic
resume_skills = ["python", "machine learning", "data analysis"]
job_required_skills = ["python", "sql", "machine learning"]

matched_skills = set(resume_skills).intersection(job_required_skills)

print("Matched Skills:", matched_skills)
