from configparser import ConfigParser
from urllib.parse import urlparse, parse_qs

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()

    parser.read(filename)
 
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

def get_yt_id(url):        
    query = urlparse(url)
    
    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError

def ch_epoch(seconds):
    seconds = int(seconds)
    if seconds < 60:
        return (str(seconds) + ' seconds')
    elif seconds < 60 * 60:
        return (str(seconds // 60) + ' minutes')
    elif seconds < 24 * 60 * 60:
        return (str(seconds // (60 * 60)) + ' hours')
    elif seconds < 30 * 24 * 60 * 60:
        return (str(seconds // (24 * 60 * 60)) + ' days')
    elif seconds < 12 * 30 * 24 * 60 * 60:
        return (str(seconds // (30 * 24 * 60 * 60)) + ' months')
    else:
        return (str(seconds // (12 * 30 * 24 * 60 * 60)) + ' years')


