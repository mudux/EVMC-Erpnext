from collections import defaultdict
import difflib
# Program to compare key text to a test text
# and returns matching success rate
atxt = "NELSON PKEMOI SHIkoli"  # key text
btxt = "NELSON PKEMOI SHIkoli"  # comparative text

aarr = atxt.split()
barr = btxt.split()
alen = len(aarr)
blen = len(barr)
rates = defaultdict(dict)
length = 0
maximum = 0.0
high = 0.0
exprfoundat = -1

for aelm in aarr:
    high = 0.0
    for belm in barr:
        seq = difflib.SequenceMatcher(None, a=aelm.lower(), b=belm.lower())
        d = seq.ratio()*100
        d = round(d, 1)
        try:
            exprfoundat = aelm.lower().find(belm.lower())
            print "Expression found at: "+str(exprfoundat)+"with rate: "+str(d)
        except Exception as e:
            pass
        if exprfoundat != -1 and d < 100:
            rates[aelm][belm] = 100
        else:
            rates[aelm][belm] = d
    for key, value in rates[aelm].items():
        if value > high:
            high = value
    maximum = maximum + high
length = alen
maximum = maximum/length
print(str(maximum))

# default_timeout = 300
# queue_timeout = {
# 	'background': 2500,
# 	'long': 1500,
# 	'default': 300,
# 	'short': 300
# }

# redis_connection = None

# def enqueue(method, queue='default', timeout=None, event=None,
# 	is_async=True, job_name=None, now=False, enqueue_after_commit=False, **kwargs):

# Enqueue method to be executed using a background worker
# :param method: method string or method object
# :param queue: should be either long, default or short
# :param timeout: should be set according to the functions
# :param event: this is passed to enable clearing of jobs from queues
# :param is_async: if is_async=False, the method is executed immediately, else via a worker
# :param job_name: can be used to name an enqueue call, which can be used to prevent duplicate calls
# :param now: if now=True, the method is executed via frappe.call
# :param kwargs: keyword arguments to be passed to the method