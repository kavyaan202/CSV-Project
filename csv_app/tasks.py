from celery import shared_task
import pandas as pd

@shared_task
def process_csv(file_path):
    data = pd.read_csv(file_path)
    numeric_cols = data.select_dtypes(include=['number'])
    
    results = {
        "sum": numeric_cols.sum().to_dict(),
        "average": numeric_cols.mean().to_dict(),
        "count": numeric_cols.count().to_dict()
    }
    
    return results
