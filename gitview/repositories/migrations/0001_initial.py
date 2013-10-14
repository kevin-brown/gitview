# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repository'
        db.create_table(u'repositories_repository', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('owner_ct', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('location', self.gf('django.db.models.fields.FilePathField')(path='/home/git/repositories/', max_length=100, recursive=True, match='.*\\.git')),
        ))
        db.send_create_signal(u'repositories', ['Repository'])


    def backwards(self, orm):
        # Deleting model 'Repository'
        db.delete_table(u'repositories_repository')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'repositories.repository': {
            'Meta': {'object_name': 'Repository'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.FilePathField', [], {'path': "'/home/git/repositories/'", 'max_length': '100', 'recursive': 'True', 'match': "'.*\\\\.git'"}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'owner_ct': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'owner_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['repositories']