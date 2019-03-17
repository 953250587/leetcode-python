"""
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

    graph will have length at most 10000.
    The number of edges in the graph will not exceed 32000.
    Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].

"""


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        371ms
        """
        result = set()
        # used = set()
        cant = set()
        def dfs(node, cur):
            if node in cur:
                return True
            if node in cant:
                return True
            if node in result:
                return False
            cur.add(node)
            for next_node in graph[node]:
                if dfs(next_node, cur):
                    cant.add(next_node)
                    return True
            cur.remove(node)
            result.add(node)
            return False
        for node in range(len(graph)):
            cur = set()
            if node not in cant or node not in result:
                dfs(node, cur)
        # print(cant)
        return sorted(list(result))

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        550ms
        """
        import collections
        n = len(graph)
        out_degree = collections.defaultdict(int)
        in_nodes = collections.defaultdict(list)
        queue = []
        ret = []
        for i in range(n):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                queue.append(i)
            for j in graph[i]:
                in_nodes[j].append(i)
        while queue:
            term_node = queue.pop(0)
            ret.append(term_node)
            for in_node in in_nodes[term_node]:
                out_degree[in_node] -= 1
                if out_degree[in_node] == 0:
                    queue.append(in_node)
        return sorted(ret)
print(Solution().eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))
print(Solution().eventualSafeNodes([[114,238,443,463],[433],[172,318,409,443],[25,141,196,331],[199],[],[209,265,286,472],[87,186,191],[136,158,335],[134,295],[98,236,422],[68,186],[33,88,155,300],[97,146,174,229,427,443],[199,456,464,466],[381,475],[6,48,108,137,350],[309,472],[147,164,459,465],[306],[21,55,194,213,221,258],[124,254,258],[246,249,419,430],[209,453],[28,156,229],[103,169,412,416],[],[52,65,199,411],[45,50,237,491],[78,159,264,364,469],[208,403],[113,341],[75,118,265,430],[233,239,313],[250,300,435],[107,165,286,316,335,362],[156,310,388],[],[16,302,318],[192,289,451],[20,126,141,350,395],[76,110,190,465,487],[245,342,382],[255,356],[125,389],[82,228,296,403,443,477],[25,222,225],[408],[285,386],[453],[],[52,117,241,343,349,421],[101,119,129,235,352,479],[],[188],[91,156,377,388,444],[260,294,450,461],[247,254],[139,167,307,418,478],[77,222,467],[205,282,288,346,377],[],[233],[124,188],[120,132,153,328,345],[343],[79,269,370,422,431],[],[336,348,363,394,402],[223,323,391,456],[150,238,265,370,393,421],[],[249],[95,134,220,380,451],[267,382,397],[210,276,299,436,454,495],[99,212,299,336],[83,243,264],[83,149,276,337,351,415],[259,378],[182,310],[156,247,262,435],[108,265],[99,312,333,381,448],[230,333,395],[341,443,490],[188,430],[108,202,430,480],[122,236,424],[215,250,313,386],[106,136,248,306,337],[209,331,381,432],[277,299,461,495],[328,344,373,436,482],[121,175,187,457,474,492],[165],[330],[192],[190,307,483],[137,230,369],[],[228,467],[281,402,441,488],[328,348,407,428,441,457],[208,258,259,349,384,419],[25,130,320],[491],[198,244,251,332,373],[237,464],[53,136,143],[210,450],[233,325,363,380,385],[481],[],[126,179,236,309,472,475],[474],[240,256,304],[141,166],[198,238,259,288,420],[],[332,345],[144,253,316,424],[145,148,206,239,338,375],[189,233,296,414,417],[217,340],[453],[179,337,361,366],[135,146,192,211,287,452],[182],[205,370,410,492],[134,178,415,438,443],[162,403,440,441],[326],[],[135,196,210,360,397,482],[442],[209,275,308,342,407,423],[],[239,405],[416,428],[246,281,408,467,479],[334,423,440,446],[151,191,279,314,412,413],[],[196,352,451,493,495],[210,271],[345,378,402],[161,388,418,424,499],[253,315,392],[331,395],[458],[154],[238],[221,440],[298,330,419,441,491,498],[198,441,444],[],[167,279,339,346],[],[229,230,304,324,327,391],[212,286,318,430,463,471],[],[227,438],[213,430],[198,304,434,452],[226,432],[264,270,338,351,365,492],[],[169,222,409,443,474],[355,415],[],[219,243,310,361,450,453],[],[],[212,229],[253,362,394,448],[178,229,237,321,386,446],[407],[201,202,258,300,401,415],[],[405,436],[239,325,415,457],[],[439,482],[301,454],[468,489],[250,277,380,436,445],[192,407,424,428,476],[349,408,427],[],[327,348,452],[285,391,397,437],[196,305,397,464],[224,257,340,397,401,449],[238,337,435,459,467],[402,457,475],[],[364],[228,233,445,455],[283,435,439,496],[392,488,491],[208,404,461,468],[],[],[250,463],[250,432],[5,214,238,247,293,385],[14,236,297,324,360,371],[284,327,429,470],[211,290,351,485],[271,275,377,400],[312],[241,328,354,379],[343,429],[267,275,442,486,493],[225,290,335,451],[217,252,260,305,474],[285,314,322,360,362,427],[331],[320,412],[307,398,448],[371,403,441],[235,243,298,394,462],[234,268,294,295,407,467],[234,312,415,456],[288,414,415],[283],[],[309,400,422,436,471,493],[235,449],[],[495],[324,381,383,464,476],[349],[397,403],[334,376,380,386],[254,398,462],[391],[244,249,259,321,323,448],[430,452,465],[260,282,294,350,371,476],[],[257,299,368,425,434],[],[251,328,392,396,428,448],[],[396,432,462,485],[256,259,341,383,392,458],[281,317,319,346,450,473],[311,407,419,433,492],[],[281,333,334,462,495],[254,284,302,351,434],[],[289,295,302,308],[286,362,369,408,411,461],[343],[279,314,332,440,441,454],[291,302,308,368,412],[346],[],[337,392,459,463,483],[281,339,360,373,380,450],[295,317,346,472],[443,463],[187,474,498],[297,340,366,396,461,477],[389,397,427,430],[301],[379],[454],[301],[],[315,337,399,474],[306,363,425,488],[371,427],[277,321,377],[304,310,388,435,464,483],[381,427],[303,308,418,425,474,499],[],[363,409,428,480,482],[320,356],[290,472,475],[142,335],[377,404,495],[315,359,378,430,486,487],[312],[],[],[304,326],[315,347,385,413,414,497],[296,328,417,497],[297,300,320,436,490],[313,459,490],[375,394,430,457,469,488],[172,392,457],[452,458,498],[354,410,415,442,458],[357],[315,334,348,384,473,498],[],[314,351,412],[140,347,447,450],[329,334,382,415,470,494],[],[345,349,390,395,443],[],[337,359,382,390,447],[314,477],[412],[107],[341,396],[],[350,374],[92],[327],[258,479],[319,345,360,385,398,451],[375,395,398,417,467],[385,402,410,450,466],[353,455,492],[473],[330,491],[336,345,376,471],[],[261,343,359,493],[440],[408,454],[396,439,474],[367,405,410],[402],[39,350,368],[339,352,403,407,496],[227,442],[],[338,349,359,398,403,486],[],[345,378,436,451],[],[398,418,455],[353,411,466],[484],[365,409,421,476],[],[372,421,432,434,454],[357,460],[352,353,381,409,427],[352,398,405,453,464,472],[370,403,493],[463],[423,426],[458],[],[380,421,425,460,479],[384,426,436,464],[381,399,451,493],[390,407,482,492],[427,431,444,448,488,489],[411],[382,396,413,424,426,443],[363,383,492],[481,492,497],[381,419,429,467,470,481],[237,381,388,401,403,414,471],[380,399,422,424,441,447],[377,457],[419,461,473,489],[376,407,459],[],[416,479],[390,427,468,492],[373],[379,385,398,401],[446,459,471,475],[376,395,413,421,428],[380,408,440,446,447],[444],[416,461],[449,457,476,482],[],[461],[389,429,476],[387,390,392,459,473,480],[407,463,472,485],[433,434,460],[390,395,398,412,427],[416,420,479],[450,469,470,499],[407,408,437,464,491,494],[428,446,496],[419,459,463,492],[397,410,422,444],[445],[426,451,467],[],[409,412],[412,419,432,457,466],[449],[],[],[452,455],[383,432,449,473],[457],[444],[412,419,450,456,458,465],[426,450,467,480,494],[],[409,451,494],[454,481,493,497,499],[416,427,434],[438,486,487,497],[439,497],[422,431,437,471,475],[439,473],[428,431,457,490],[440,448,470],[202,455,484],[445,458],[463,475],[437,469,481,499],[442,453,459,488,490,498],[],[435,441,444,465,484,491],[434,466],[444,453,468,486,497],[429,451,461,479,483],[430,431,439],[280,439,442,445,482,484],[434,458,486,487,488],[445,474,480,482,484,494],[433,439,471],[438,444,445,456,464],[456,462,469],[454,460,471,493,499],[465,477],[464,480,485,486,497],[442,470,472,473,476,496],[453,465,466,469,495],[452,488,494],[443,446,475,492,498],[479,484,485],[449,466,478],[],[445,460,471,477,489],[446,466,475,483,486,496],[449,456],[484,495],[451,453,454,458,476],[496],[471,494],[463,492],[453,454,478,487,493],[462,463,469,484],[477],[468,495,496],[457,461,463,485,495],[461,462,463,465,477],[480,488,493,496],[479,480,489,493],[469,487],[478],[],[],[],[481],[474,478,492],[470,484,488,491],[],[481,486,487],[483,485,488],[476,477,484],[473,474,475,478,480,494],[478,498],[],[],[487,492,498],[481,484,488,489,495,496],[],[486,488,489,492,494,495],[487,488,497],[492],[489],[486],[485,488,490,491,492,495],[486,489,492,493,494],[487,493,499],[493,495,496,497,498],[497,498],[494,495,496,498],[491,492,497,498],[492,493,494,498],[495,496],[494,495,496,497,498,499],[495,497,498,499],[496,497,498,499],[497],[498,499],[],[]]))




