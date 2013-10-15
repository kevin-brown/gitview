# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Repository.default_branch'
        db.add_column(u'repositories_repository', 'default_branch',
                      self.gf('django.db.models.fields.SlugField')(default='master', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Repository.default_branch'
        db.delete_column(u'repositories_repository', 'default_branch')


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
            'default_branch': ('django.db.models.fields.SlugField', [], {'default': "'master'", 'max_length': '100'}),
            'has_issues': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'location': ('django.db.models.fields.FilePathField', [], {'path': "'/home/git/repositories/'", 'max_length': '100', 'recursive': 'True', 'match': "'.*\\\\.git'"}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'owner_ct': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'owner_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['repositories']