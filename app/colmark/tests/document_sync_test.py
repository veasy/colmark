import unittest

from socketIO_client import SocketIO, BaseNamespace, LoggingNamespace
from base_test_case import BaseTestCase
from colmark import config
from colmark.routes.document import DOCUMENT_NAMESPACE

__author__ = 'cansik'


class DocumentNamespace(LoggingNamespace):
    _connected = True

    def on_connect(self):
        print('connected')

    def on_error(self, data):
        print('error')

    def on_echo_response(self, *args):
        print('echo_response', args)


class DocumentSyncTest(BaseTestCase):
    def setUp(self):
        super(DocumentSyncTest, self).setUp()
        self.client = SocketIO('localhost', config.SERVER_PORT, DocumentNamespace)
        self.doc = self.client.define(DocumentNamespace, DOCUMENT_NAMESPACE)

    def tearDown(self):
        super(DocumentSyncTest, self).tearDown()
        self.client.disconnect()

    def test_single_client(self):
        self.doc.emit('echo', 'hello world')
        print('sent echo')
        self.client.wait(seconds=1)


if __name__ == '__main__':
    unittest.main()
