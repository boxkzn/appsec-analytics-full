from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import httpx

retry_http = retry(
    reraise=True,
    retry=retry_if_exception_type(httpx.HTTPError),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=0.5, min=1, max=8),
)
