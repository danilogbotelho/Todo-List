from zope.interface import Interface
from zope import schema
import grok
from megrok import layout
from megrok.scaffold import Controller, scaffold, require as scaffold_require

from todolist import resource

class Todolist(grok.Application, grok.Container):
    pass

class Layout(layout.Layout):
    grok.context(Interface)
    
    def update(self):
        resource.style.need()

class ITodoItem(Interface):
    title = schema.TextLine(title=u'Title')
    done = schema.Choice(title=u'Already done?', values=['yes', 'no'])

class TodoItem(grok.Model):
    grok.implements(ITodoItem)
    
    title = u''
    done = u'no'

class TodoCtrl(Controller):
    grok.context(Todolist)
    
    scaffold(TodoItem, listname='index', aspage=True)
    
    #CUSTOM CODE -- None of the below is required!
        
    scaffold_require(add='zope.ManageContent', edit='zope.ManageContent')
    
    start_batching_at = 10
    batch_size = 10
    
    def update(self):
        if self.view.__form_type__ == 'list':
            self.view.cssClassEven = u'odd'
            self.view.cssClassOdd = u'even'
    
    @grok.action('Cancel', Controller.edit_actions)
    def cancel(self, **data):
        self.view.redirect(self.view.url(self.view.context))
        
    @grok.action('Populate', Controller.list_actions)
    def populate(self, **data):
        start_i = len(self.context)
        n = 0
        while n < 25:
            i = n+start_i
            title = 'Something to do %d' % (i+1)
            try:
                ti = TodoItem()
                ti.title = title
                ti.done = ['yes', 'no'][i%2==1]
                self.context[str(i+1)] = ti
                n+=1
            except KeyError:
                start_i += 1
        
        self.view.status = '25 new items added.'
        self.view.updateAfterActionExecution()