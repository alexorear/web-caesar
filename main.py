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

def build_page(textarea_content):
    # html boilerplate for the top of every page
    page_header = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Web-Caesar</title>
            </head>
            <body>
                <h2>Web-Caesar</h2>"""

    # html boilerplate for the bottom of every page
    page_footer = """
        </body>
        </html>"""

    # page content
    rot_label = "<label> Rotate by: </label>"
    rot_input = "<input type='number' name='rot'/>"

    text_label = "<label>Type a message: </label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"

    submit = "<input type='submit'/>"
    form = ("<form method='post'>" +
            rot_label + rot_input + "<br>" +
            "<br>" + text_label + textarea + "<br>" +
            "<br>" + submit + "</form>")

    return page_header + form + page_footer

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rot = self.request.get("rot")
        encrypted_message = caesar.encrypt(message, rot)

        content =build_page(encrypted_message)

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
