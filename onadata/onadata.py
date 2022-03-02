import pkg_resources
import pandas as pd

#####################################################################
# Below is a list of all the functions which return datasets by name
#####################################################################

def list_sets():
    """Lists the data set names. All the data sets can be saved as a data frame by calling the names as methods."""
    
    return ['caviar_end', 'caviar_middle', 'caviar_start',
  'chinook_customers', 'chinook_employees', 'chinook_invoices', 
  'chinook_items', 'dolphins', 'email_edgelist', 'email_vertices', 
  'eu_referendum', 'friends_tv_edgelist', 'g14_edgelist', 'karate', 
  'koenigsberg', 'lesmis', 'londontube_edgelist', 'londontube_vertices', 
  'madmen_edges', 'madmen_vertices', 'netscience', 'ontariopol_vertices', 
  'ontariopol_edgelist', 'park_reviews', 'pizza', 's50_edges', 's50_vertices', 
  'schoolfriends_edgelist', 'schoolfriends_vertices', 'wikivote', 
  'workfrance_vertices', 'workfrance_edgelist']

# caviar_end
def caviar_end():
    """Return the caviar_end dataframe.

    Contains the following fields:
         #   Column           Non-Null Count  Dtype 
        ---  ------           --------------  ----- 
         0   from             72 non-null     object 
         1   to               72 non-null     object 
         2   weight           72 non-null     int64 
         
    """
    stream = pkg_resources.resource_stream(__name__, 'data/caviar_end.csv')
    return pd.read_csv(stream)
  
# caviar_middle
def caviar_middle():
    """Return the caviar_middle dataframe.

    Contains the following fields:
         #   Column           Non-Null Count  Dtype 
        ---  ------           --------------  ----- 
         0   from             50 non-null     object 
         1   to               50 non-null     object 
         2   weight           50 non-null     int64 
         
    """
    stream = pkg_resources.resource_stream(__name__, 'data/caviar_middle.csv')
    return pd.read_csv(stream)
  
# caviar_start
def caviar_start():
    """Return the caviar_start dataframe.

    Contains the following fields:
         #   Column           Non-Null Count  Dtype 
        ---  ------           --------------  ----- 
         0   from             26 non-null     object 
         1   to               26 non-null     object 
         2   weight           26 non-null     int64 
         
    """
    stream = pkg_resources.resource_stream(__name__, 'data/caviar_start.csv')
    return pd.read_csv(stream)


# chinook_customers
def chinook_customers():
    """Return the chinook_customers dataframe.

    Contains the following fields:
         #   Column       Non-Null Count  Dtype
        ---  ------       --------------  -----
         0   CustomerId   59 non-null     int64
         1   FirstName    59 non-null     object
         2   LastName     59 non-null     object
         3   SupportRepId 59 non-null     int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/chinook_customers.csv')
    return pd.read_csv(stream)
  
# chinook_employees
def chinook_employees():
    """Return the chinook_employees dataframe.

    Contains the following fields:
         #   Column       Non-Null Count  Dtype
        ---  ------       --------------  -----
         0   EmployeeId   8 non-null     int64
         1   FirstName    8 non-null     object
         2   LastName     8 non-null     object
         3   ReportsTo    8 non-null     int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/chinook_employees.csv')
    return pd.read_csv(stream)

# chinook_invoices
def chinook_invoices():
    """Return the chinook_invoices dataframe.

    Contains the following fields:
         #   Column       Non-Null Count  Dtype
        ---  ------       --------------  -----
         0   InvoiceId    412 non-null    int64
         1   CustomerId   412 non-null    int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/chinook_invoices.csv')
    return pd.read_csv(stream)

# chinook_items
def chinook_items():
    """Return the chinook_items dataframe.

    Contains the following fields:
         #   Column       Non-Null Count  Dtype
        ---  ------       --------------  -----
         0   InvoiceId    2240 non-null   int64
         1   TrackId      2240 non-null   int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/chinook_items.csv')
    return pd.read_csv(stream)

# dolphins
def dolphins():
    """Return the dolphins dataframe.
    
    Contains the following fields:
    
         #   Column          Non-Null Count  Dtype 
        ---  ------          --------------  ----- 
         0   from            159 non-null    object
         1   to              159 non-null    object

    """
    stream = pkg_resources.resource_stream(__name__, 'data/dolphins.csv')
    return pd.read_csv(stream)

# email_edgelist
def email_edgelist():
    """Return the email_edgelist dataframe
    
    Contains the following fields:
    
         #   Column     Non-Null Count  Dtype 
        ---  ------     --------------  ----- 
         0   from       24929 non-null  int64
         1   to         24929 non-null  int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/email_edgelist.csv')
    return pd.read_csv(stream)

# email_vertices
def email_vertices():
    """Return the email_vertices dataframe
    
    Contains the following fields:
    
         #   Column     Non-Null Count  Dtype 
        ---  ------     --------------  ----- 
         0   id         1005 non-null   int64
         1   dept       1005 non-null   int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/email_vertices.csv')
    return pd.read_csv(stream)

# eu_referendum
def eu_referendum():
    """Return the eu_referendum dataframe
    
    Contains the following fields:
    
        #   Column              Non-Null Count  Dtype  
        ---  ------             --------------  -----  
         0   Region             382 non-null    object 
         1   Area_Code          382 non-null    object 
         2   Remain             382 non-null    int64
         3   Leave              382 non-null    int64 

    """
    stream = pkg_resources.resource_stream(__name__, 'data/eu_referendum.csv')
    return pd.read_csv(stream)

# friends_tv_edgelist
def friends_tv_edgelist():
    """Return the friends_tv_edgelist dataframe
    
    Contains the following fields:
    
        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     2976 non-null   object
         1   to       2976 non-null   object
         2   weight   2976 non-null   int64
 
    """
    stream = pkg_resources.resource_stream(__name__, 'data/friends_tv_edgelist.csv')
    return pd.read_csv(stream)

# g14_edgelist
def g14_edgelist():
    """Return the g14_edgelist dataframe
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     18 non-null     int64
         1   to       18 non-null     int64
         2   weight   18 non-null     int64    

    """
    stream = pkg_resources.resource_stream(__name__, 'data/g14_edgelist.csv')
    return pd.read_csv(stream)

# karate
def karate():
    """Return the karate dataframe
    
    Contains the following fields:
    
        #   Column        Non-Null Count  Dtype 
        ---  ------       --------------  ----- 
         0   from         78 non-null     object
         1   to           78 non-null     object 

    """
    stream = pkg_resources.resource_stream(__name__, 'data/karate.csv')
    return pd.read_csv(stream)

# koenigsberg
def koenigsberg():
    """Return the koenigsberg dataframe
    
    Contains the following fields:
      
        #   Column        Non-Null Count  Dtype 
        ---  ------       --------------  ----- 
         0   from         7 non-null     object
         1   to.          7 non-null     object 
    
    """
    stream = pkg_resources.resource_stream(__name__, 'data/koenigsberg.csv')
    return pd.read_csv(stream)

# lesmis
def lesmis():
    """Return the lesmis dataframe
    
    Contains the following fields:
    
        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     254 non-null     object
         1   to       254 non-null     object
         2   weight   254 non-null     int64   
    """
    stream = pkg_resources.resource_stream(__name__, 'data/lesmis.csv')
    return pd.read_csv(stream)

# londontube_edgelist
def londontube_edgelist():
    """Return the londontube_edgelist dataframe
    
    Contains the following fields:
    
          #   Column    Non-Null Count  Dtype
        ---  ------     --------------  -----
         0   from       406 non-null    int64
         1   to         406 non-null    int64
         2   line       406 non-null    object
         3   linecolor  406 non-null    object
         
    """
    stream = pkg_resources.resource_stream(__name__, 'data/londontube_edgelist.csv')
    return pd.read_csv(stream)
  
# londontube_vertices
def londontube_vertices():
    """Return the londontube_vertices dataframe
    
    Contains the following fields:
    
          #   Column    Non-Null Count  Dtype
        ---  ------     --------------  -----
         0   id         302 non-null    int64
         1   name       302 non-null    object
         2   latitude   302 non-null    float64
         3   longitude  302 non-null    float64
         
    """
    stream = pkg_resources.resource_stream(__name__, 'data/londontube_vertices.csv')
    return pd.read_csv(stream)


# madmen_edges
def madmen_edges():
    """Return the madmen_edges dataframe.

    Contains the following fields:
         #   Column         Non-Null Count  Dtype  
        ---  ------         --------------  -----  
         0   Name1          39 non-null     object
         1   Name2          39 non-null     object  
         2   Married        39 non-null     int64 

    """
    stream = pkg_resources.resource_stream(__name__, 'data/madmen_edges.csv')
    return pd.read_csv(stream)
  
# madmen_vertices
def madmen_vertices():
    """Return the madmen_vertices dataframe.

    Contains the following fields:
         #   Column         Non-Null Count  Dtype  
        ---  ------         --------------  -----  
         0   label          45 non-null     object
         1   Gender         45 non-null     object  
         2   Main           45 non-null     int64 

    """
    stream = pkg_resources.resource_stream(__name__, 'data/madmen_vertices.csv')
    return pd.read_csv(stream)

# netscience
def netscience():
    """Return the netscience dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     2742 non-null   object
         1   to       2742 non-null   object
         2   weight   2742 non-null   float64  

    """
    stream = pkg_resources.resource_stream(__name__, 'data/netscience.csv')
    return pd.read_csv(stream)

# ontariopol_edgelist
def ontariopol_edgelist():
    """Return the ontariopol_edgelist dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     6095 non-null   int64
         1   to       6095 non-null   int64
         2   weight   6095 non-null   int64  

    """
    stream = pkg_resources.resource_stream(__name__, 'data/ontariopol_edgelist.csv')
    return pd.read_csv(stream)
  
# ontariopol_vertices
def ontariopol_vertices():
    """Return the ontariopol_vertices dataframe.
    
    Contains the following fields:

        #   Column        Non-Null Count  Dtype  
        ---  ------       --------------  -----
         0   id            6095 non-null  int64
         1   screen_name   6095 non-null  object
         2   name          6095 non-null  object 
         3   party         6095 non-null  object 

    """
    stream = pkg_resources.resource_stream(__name__, 'data/ontariopol_vertices.csv')
    return pd.read_csv(stream)

# park_reviews
def park_reviews():
    """Return the park_reviews dataframe.
    
    Contains the following fields:
         #   Column    Non-Null Count  Dtype
        ---  ------    --------------  -----
         0   park_id   231 non-null    object
         1   user_id   231 non-null    object
         2   park_name 231 non-null    object
         3   stars.    231 non-null    int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/park_reviews.csv')
    return pd.read_csv(stream)

# pizza
def pizza():
    """Return the pizza dataframe.
    
    Contains the following fields:
         #   Column                 Non-Null Count  Dtype  
        ---  ------                 --------------  -----  
         0   requester              400 non-null    object 
         1   responder              400 non-null    object  
         2   request_id             400 non-null    object
         3   requester_votes        400 non-null    int64  
         4   requester_subreddits   400 non-null    int64  

    """
    stream = pkg_resources.resource_stream(__name__, 'data/pizza.csv')
    return pd.read_csv(stream)
  
# s50_edges
def s50_edges():
    """Return the s50_edges dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     122 non-null    object
         1   to       122 non-null    object

    """
    stream = pkg_resources.resource_stream(__name__, 'data/s50_edges.csv')
    return pd.read_csv(stream)
  
  
# s50_vertices
def s50_vertices():
    """Return the s50_vertices dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   id       122 non-null    object
         1   smoke    122 non-null    int64
         2   alcohol  122 non-null    int64
         3   drugs    122 non-null    int64
         4   sport    122 non-null    int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/s50_vertices.csv')
    return pd.read_csv(stream)
  
# schoolfriends_edgelist
def schoolfriends_edgelist():
    """Return the schoolfriends_edgelist dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     2105 non-null   int64
         1   to       2105 non-null   int64
         2   type     2105 non-null   object

    """
    stream = pkg_resources.resource_stream(__name__, 'data/schoolfriends_edgelist.csv')
    return pd.read_csv(stream)
  
# schoolfriends_vertices
def schoolfriends_vertices():
    """Return the schoolfriends_vertices dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   id       329 non-null    int64
         1   class    329 non-null    object
         2   gender   329 non-null    object

    """
    stream = pkg_resources.resource_stream(__name__, 'data/schoolfriends_vertices.csv')
    return pd.read_csv(stream)
  
# wikivote
def wikivote():
    """Return the wikivote dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     103688 non-null int64
         1   to       103688 non-null int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/wikivote.csv')
    return pd.read_csv(stream)

# workfrance_edgelist
def workfrance_edgelist():
    """Return the workfrance_edgelist dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   from     932 non-null    int64
         1   to       932 non-null    int64
         2   mins     932 non-null    int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/workfrance_edgelist.csv')
    return pd.read_csv(stream)
  
# workfrance_edgelist
def workfrance_vertices():
    """Return the workfrance_vertices dataframe.
    
    Contains the following fields:

        #   Column    Non-Null Count  Dtype  
        ---  ------   --------------  -----
         0   id       211 non-null    int64
         1   dept     211 non-null    object

    """
    stream = pkg_resources.resource_stream(__name__, 'data/workfrance_vertices.csv')
    return pd.read_csv(stream)
 
 
  
