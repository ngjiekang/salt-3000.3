import salt.config
import salt.netapi
import salt.utils.files
import salt.utils.platform
import salt.utils.pycrypto

from tests.support.paths import TMP_CONF_DIR, TMP
from tests.support.runtests import RUNTIME_VARS

from flask import Flask, request
app = Flask(__name__)

@app.route("/files/<expression>")
def analyze_file(expression):
  opts = salt.config.client_config(os.path.join(RUNTIME_VARS.TMP_CONF_DIR, 'master'))
  s = salt.netapi.NetapiClient(opts)
  s.run(expression)
