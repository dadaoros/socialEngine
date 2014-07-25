# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'socialApp_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'socialApp', ['Profile'])

        # Adding M2M table for field followers on 'Profile'
        m2m_table_name = db.shorten_name(u'socialApp_profile_followers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_profile', models.ForeignKey(orm[u'socialApp.profile'], null=False)),
            ('to_profile', models.ForeignKey(orm[u'socialApp.profile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_profile_id', 'to_profile_id'])

        # Adding M2M table for field followings on 'Profile'
        m2m_table_name = db.shorten_name(u'socialApp_profile_followings')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_profile', models.ForeignKey(orm[u'socialApp.profile'], null=False)),
            ('to_profile', models.ForeignKey(orm[u'socialApp.profile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_profile_id', 'to_profile_id'])

        # Adding model 'Pub'
        db.create_table(u'socialApp_pub', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['socialApp.Profile'])),
            ('pub_text', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'socialApp', ['Pub'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'socialApp_profile')

        # Removing M2M table for field followers on 'Profile'
        db.delete_table(db.shorten_name(u'socialApp_profile_followers'))

        # Removing M2M table for field followings on 'Profile'
        db.delete_table(db.shorten_name(u'socialApp_profile_followings'))

        # Deleting model 'Pub'
        db.delete_table(u'socialApp_pub')


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
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'pub_text': ('django.db.models.fields.CharField', [], {'max_length': '350'})
        }
    }

    complete_apps = ['socialApp']