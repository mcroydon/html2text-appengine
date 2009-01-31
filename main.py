from html2text import html2text

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
      <html>
        <body>
          <h3>Convert HTML to text</h3>
          <form action="/convert" method="post">
            <div><textarea name="content" rows="10" cols="80"></textarea></div>
            <div><input type="submit" value="Go!"></div>
          </form>
          <p>Uses Aaron Swartz' <a href="http://www.aaronsw.com/2002/html2text/">html2text</a>.</p>
        </body>
      </html>""")


class Convert(webapp.RequestHandler):
  def post(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(html2text(self.request.get('content')))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/convert', Convert)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()