from app import create_app
import pytest
 
app = create_app('testing')

@app.cli.command()
def test():
    import unittest
    import sys
 
    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.errors or result.failures:
        sys.exit(1)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4034)