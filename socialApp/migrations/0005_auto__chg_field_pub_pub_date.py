# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Pub.pub_date'
        db.alter_column(u'socialApp_pub', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Pub.pub_date'
        db.alter_column(u'socialApp_pub', 'pub_date', self.gf('django.db.models.fields.DateField')())

    models = {
        u'socialApp.profile': {
            'Meta': {'object_name': 'Profile'},
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Followers'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['socialApp.Profile']"}),
            'followings': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Followings'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['socialApp.Profile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'socialApp.pub': {
            'Meta': {'object_name': 'Pub'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['socialApp.Profile']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'pub_text': ('django.db.models.fields.CharField', [], {'max_length': '350'})
        }
    }

    complete_apps = ['socialApp']