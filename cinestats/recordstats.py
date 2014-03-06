import pgdb

class RecordStats:
   """A simple class to provide the statistical information to populate
      a  cinefiles report. 
   """

   def __init__(self, host='cinefiles.cspace.berkeley.edu'):
      self.HOST = host
      self.DBNAME='cinefiles_domain'
      self.USER='reporter'
      self.PW = 'csR2p4rt2r'

      self.connect_string = "%s:%s:%s:%s" % (
         self.HOST,self.DBNAME, self.USER, self.PW)

   def getConn(self):
      conn = pgdb.connect( self.connect_string )   
      return conn

   def getCount(self, query):
      conn = self.getConn()

      if not conn:
         return None

      cur = conn.cursor()
      cur.execute( query )
      res = cur.fetchone()[0]
      cur.close()
      conn.close()   
      return res         
      
   def getDocCount(self):
      query = """SELECT count(1)
                 FROM collectionobjects_common cc
                 INNER JOIN misc m 
                    ON (m.id = cc.id
                        AND m.lifecyclestate <> 'deleted'
                        AND cc.collection = 'urn:cspace:cinefiles.cspace.berkeley.edu:vocabularies:name(collection):item:name(cinefiles)''CineFiles''')"""
      return self.getCount(query)

   def getDocYTD(self):
      query = """SELECT count(1)
                 FROM collectionspace_core c
                 INNER JOIN misc m
                    ON (c.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND c.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:collectionobjects:%'
                        AND  c.createdat > to_date(date_part('year', now())||'-01-01', 'YYYY-MM-DD'))"""
      return self.getCount(query)

   def getNameCount(self):
      query = """SELECT count(1)
                 FROM hierarchy h
                 INNER JOIN persons_common p
                    ON (h.id = p.id 
                        AND p.inauthority = 'ae43b316-d4ff-475f-921c')
                 INNER JOIN misc m
                    ON (h.id = m.id
                        AND m.lifecyclestate <> 'deleted')"""
      return self.getCount(query)

   def getNameYTD(self):
      query = """SELECT count(1)
                 FROM collectionspace_core c
                 INNER JOIN misc m
                    ON (c.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND c.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:personauthorities:name(person):item:name(%'
                        AND  c.createdat > to_date(date_part('year', now())||'-01-01', 'YYYY-MM-DD'))"""
      return self.getCount(query)

   def getOrgCount(self):
      query = """SELECT count(1)
                 FROM organizations_common oc
                 INNER JOIN misc m
                    ON (oc.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND oc.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:orgauthorities:name(organization):item:name(%')"""
      return self.getCount(query)

   def getOrgYTD(self):
      query = """SELECT count(1)
                 FROM collectionspace_core c
                 INNER JOIN misc m
                    ON (c.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND c.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:orgauthorities:name(organization):item:name(%'
                        AND  c.createdat > to_date(date_part('year', now())||'-01-01', 'YYYY-MM-DD'))"""
      return self.getCount(query)
 
   def getCommitteeCount(self):
      query = """SELECT count(1)
                 FROM organizations_common o
                 INNER JOIN misc m
                    ON (o.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND o.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:orgauthorities:name(committee):item:name(%')"""
      return self.getCount(query)

   def getCommitteeYTD(self):
      query = """SELECT count(1)
                 FROM collectionspace_core c
                 INNER JOIN misc m
                    ON (c.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND c.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:orgauthorities:name(committee):item:name(%'
                        AND  c.createdat > to_date(date_part('year', now())||'-01-01', 'YYYY-MM-DD'))"""
      return self.getCount(query)

   def getPageCount(self):
      query = """SELECT sum(numberofobjects)
                 FROM collectionobjects_common cc
                 INNER JOIN misc m
                    ON (cc.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND cc.collection = 'urn:cspace:cinefiles.cspace.berkeley.edu:vocabularies:name(collection):item:name(cinefiles)''CineFiles''')"""
      return self.getCount(query)

   def getPageYTD(self):
      return 6969

   def getFilmCount(self):
      query = """SELECT count(1)
                 FROM works_common w
                 INNER JOIN misc m
                    ON (w.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND w.worktype = 'urn:cspace:cinefiles.cspace.berkeley.edu:vocabularies:name(worktype):item:name(film)''Film''')"""
      return self.getCount(query)

   def getFilmYTD(self):
      query = """SELECT count(1)
                 FROM collectionspace_core c
                 INNER JOIN misc m
                    ON (c.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND c.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:workauthorities:name(work):item:name(%'
                        AND  c.createdat > to_date(date_part('year', now())||'-01-01', 'YYYY-MM-DD'))"""
      return self.getCount(query)

   def getSubjectCount(self):
      query = """SELECT count(1)
                 FROM concepts_common c
                 INNER JOIN misc m
                    ON (c.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND c.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:conceptauthorities:name(concept):item:name(%')"""
      return self.getCount(query)

   def getSubjectYTD(self):
      query = """SELECT count(1)
                 FROM collectionspace_core c
                 INNER JOIN misc m
                    ON (c.id = m.id
                        AND m.lifecyclestate <> 'deleted'
                        AND c.refname like 'urn:cspace:cinefiles.cspace.berkeley.edu:conceptauthorities:name(concept):item:name(%'
                        AND  c.createdat > to_date(date_part('year', now())||'-01-01', 'YYYY-MM-DD'))"""
      return self.getCount(query)

   def getPubWorldCount(self):
      return 5001

   def getDocWorldCount(self):
      return 10000

   def getDocWorldPages(self):
      return 20000

   def getPubEduCount(self):
      return 6002

   def getDocEduCount(self):
      return 12000

   def getDocEduPages(self):
      return 24000

   def getPubUcbCount(self):
      return 7003

   def getDocUcbCount(self):
      return 14000

   def getDocUcbPages(self):
      return 28000

   def getPubPfaCount(self):
      return 8000

   def getDocPfaCount(self):
      return 16000

   def getDocPfaPages(self):
      return  32000  

