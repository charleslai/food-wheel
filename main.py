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
import random
import os
import jinja2
import webapp2

# Jinja2 Template Directory
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = False)

# Global/Super URL Handler Class
class Handler(webapp2.RequestHandler):
    """
    Global superclass for request handlers
    """
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

# Main View Handler
class MainHandler(Handler):
    """
    Main view handler for the Collegetown food picker
    """
    def render_ctfp(self, button_title="", restaurant=""):
        # Render the main ctfp template
        self.render("ctfp.html", button_title=button_title, restaurant=restaurant)

    def get(self):
        """
        Handle get requests
        """
        self.render_ctfp("SPIN THE FUCKING WHEEL","YOU HUNGRY MOTHERFUCKER? \
                                                   CAN'T DECIDE WHAT TO EAT? \
                                                   LET US CHOOSE FOR YOU.")

    def post(self):
        # List of restaurants
        restaurants = ["Hai Hong",
                         "Vietnam",
                         "Asian Noodle House",
                         "Little Thai",
                         "Oishii Bowl",
                         "Koko",
                         "The Nines",
                         "Apollo's",
                         "Jack's",
                         "Cafe Pacific",
                         "Subway",
                         "Plum Tree",
                         "Tango Chicken",
                         "Miyake",
                         "Four Seasons",
                         "Collegetown Bagels",
                         "Collegetown Pizza",
                         "Wings Over Ithaca"]

        button_words = ["TRY THE FUCK AGAIN",
                        "I DON'T GIVE A SHIT WHAT I EAT",
                        "THIS IS SHIT",
                        "DO YOU REALLY THINK I'D EAT THIS GARBAGE",
                        "TRASH",
                        "REALLY?",
                        "I'M NOT PICKY BUT WOW THIS IS BAD"]
                         
        rindex = random.randint(0,len(restaurants)-1)
        bindex = random.randint(0,len(button_words)-1)
        rselection = restaurants[rindex]
        bselection = button_words[bindex]
        self.render_ctfp(bselection, rselection)


# Routes
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
