from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from recordstats import RecordStats

@login_required()
def index(request):
   stats = RecordStats()
   doccount = stats.getDocCount()
   docytd = stats.getDocYTD()
   personcount = stats.getNameCount()
   personytd = stats.getNameYTD()
   orgcount = stats.getOrgCount()
   orgytd = stats.getOrgYTD()
   committeecount = stats.getCommitteeCount()
   committeeytd = stats.getCommitteeYTD()
   pagecount = stats.getPageCount()
   pageytd = stats.getPageYTD()
   filmcount = stats.getFilmCount()
   filmytd = stats.getFilmYTD()
   subjcount = stats.getSubjectCount()
   subjytd = stats.getSubjectYTD()
   allnames = personcount+orgcount+committeecount

   pubworldcount = stats.getPubWorldCount()
   docworldcount = stats.getDocWorldCount()
   docworldpages = stats.getDocWorldPages()

   pubeducount = stats.getPubEduCount()
   doceducount = stats.getDocEduCount()
   docedupages = stats.getDocEduPages()

   pubucbcount = stats.getPubUcbCount()
   docucbcount = stats.getDocUcbCount()
   docucbpages = stats.getDocUcbPages()

   pubpfacount = stats.getPubPfaCount()
   docpfacount = stats.getDocPfaCount()
   docpfapages = stats.getDocPfaPages()

   template = loader.get_template('cinestats/stats.html')

   context = RequestContext(request, {
      'allnames_count': allnames,
      'allnames_ytd': personytd+orgytd+committeeytd,
      'person_count': personcount,
      'person_ytd': personytd,
      'org_count': orgcount,
      'org_ytd': orgytd,
      'committee_count': committeecount,
      'committee_ytd':committeeytd,
      'film_count': filmcount,
      'film_ytd': filmytd,
      'doc_count': doccount,
      'doc_ytd': docytd,
      'page_count': pagecount,
      'page_ytd': pageytd,
      'subject_count': subjcount,
      'subject_ytd': subjytd,
      'pub_world_count': pubworldcount,
      'doc_world_count': docworldcount,
      'doc_world_pages': docworldpages,
      'pub_edu_count': pubeducount,
      'doc_edu_count': doceducount,
      'doc_edu_pages': docedupages,
      'pub_ucb_count': pubucbcount,
      'doc_ucb_count': docucbcount,
      'doc_ucb_pages': docucbpages,
      'pub_pfa_count': pubpfacount,
      'doc_pfa_count': docpfacount, 
      'doc_pfa_pages': docpfapages,
   })
   return HttpResponse(template.render(context))
 
