from fastapi import FastAPI
from fastapi_endpoints import auto_include_routers, FastAPIApp

from . import routers

# You can use auto include routers which will give you the ability to import all
# the endpoints from the routers module (requires passing the module)
app = FastAPI()
auto_include_routers(app, routers)


# A second option is to use directly the app wrapper.
#
# This will initialize the fast api app, and auto include routers based on the
# root dir
app2 = FastAPIApp()