import unittest
import sys

from socketIO_client import SocketIO, BaseNamespace, LoggingNamespace
from base_test_case import BaseTestCase
from colmark import config
from colmark.routes.document import DOCUMENT_NAMESPACE

__author__ = 'cansik'

RECEIVED = {}

DOCUMENT_ID = 12345


def out(msg):
    sys.stderr.write('%s\n' % msg)


def on_echo_response(*args):
    out('echo_response: %s' % args)
    RECEIVED.update({'on_echo_response': True})


def on_userlist_response(*args):
    out('userlist: %s' % args)
    RECEIVED.update({'on_userlist_response': True})


def on_document_response(*args):
    out('document: %s' % args)
    RECEIVED.update({'on_document_response': True})


class DocumentNamespace(LoggingNamespace):
    _connected = True

    def on_connect(self):
        print('connected')

    def on_error(self, data):
        print('error')


class DocumentSyncTest(BaseTestCase):
    def setUp(self):
        super(DocumentSyncTest, self).setUp()
        self.client = SocketIO('localhost', config.SERVER_PORT, DocumentNamespace)
        self.doc = self.client.define(DocumentNamespace, DOCUMENT_NAMESPACE)
        global RECEIVED
        RECEIVED = {}

    def tearDown(self):
        super(DocumentSyncTest, self).tearDown()
        self.client.disconnect()

    def test_echo(self):
        self.doc.on('echo', on_echo_response)

        self.doc.emit('echo', 'hello world')
        self.client.wait(seconds=1)

        self.assertTrue(RECEIVED.get('on_echo_response', False))

    def test_single_client(self):
        self.doc.on('userlist', on_userlist_response)
        self.doc.on('document', on_document_response)

        self.doc.emit('join', {'username': 'Florian', 'document': DOCUMENT_ID})

        self.client.wait(seconds=1)

        self.doc.emit('leave', {'username': 'Florian', 'document': DOCUMENT_ID})

        self.assertTrue(RECEIVED.get('on_userlist_response', False))
        self.assertTrue(RECEIVED.get('on_document_response', False))


if __name__ == '__main__':
    unittest.main()
