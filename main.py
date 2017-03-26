#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web-Caesar</title>
</head>
<body>
    <h1>Web-Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):

        textarea = "<textarea name='message'></textarea>"
        rot_input = "<input type='number' name='rot'/>"
        submit = "<input type='submit'/>"
        form = "<form method='post'>" + rot_input + "<br>" + textarea + "<br>" + submit + "</form>"

        self.response.write(page_header + form + page_footer)

    def post(self):
        message = self.request.get("message")
        rot = self.request.get("rot")
        encrypted_message = caesar.encrypt(message, rot)
        self.response.write(page_header + "The secret message is: " + encrypted_message + page_footer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
