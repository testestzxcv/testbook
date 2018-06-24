import urllib
import pandas as pd
from itertools import count
from bs4 import BeautifulSoup
import xml.etree.ElementTree as et
import collection.crawler as cw
import re


def crawling_cu():
    results = []
