# -*- coding: utf-8 -*-
import smtplib

from django.core.mail.backends.smtp import EmailBackend
from django.core.mail.utils import DNS_NAME


class CustomEmailBackend(EmailBackend):

    def open(self):
        """
        Ensures we have a connection to the email server. Returns whether or
        not a new connection was required (True or False).
        """
        if self.connection:
            # Nothing to do if the connection is already open.
            return False
        try:
            # If local_hostname is not specified, socket.getfqdn() gets used.
            # For performance, we use the cached FQDN for local_hostname.
            fqdn_hostname = DNS_NAME.get_fqdn()
            self.connection = smtplib.SMTP(self.host, self.port,
                                           local_hostname=fqdn_hostname,
                                           timeout=self.timeout)
            if self.use_tls:
                self.connection.ehlo()
                self.connection.starttls()
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception as e:
            if not self.fail_silently:
                raise