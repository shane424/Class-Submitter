#include <iostream>
#include <set>
#include <cmath>

using namespace std;

int FindPath(const int nSartX, const int nStartY,
			 const int nTargetX, const int nTargetY,
			 const unsigned char* pMap, const int nMapWidth, const int nMapHeight,
			 int* pOutBuffer, const int nOutBufferSize);
			 
int theWork(int x, int y);
class Node;
class NodeSet;
int neighbors(Node node);
Node* findF(set<int> os, Node* start);

int main(){
	int nStartX = 0;
	int nStartY = 0;
	int nTargetX = 1;
	int nTargetY = 2;
	unsigned char pMap[] = {1,1,1,1,0,1,0,1,0,1,1,1};
	int nMapWidth = 4;
	int nMapHeight = 3;
	int pOutBuffer[12];
	int nOutBufferSize = 12;
	// FindPath(nStartX,nStartY,
			 // nTargetX,nTargetY,
			 // pMap,nMapWidth,nMapHeight,
			 // pOutBuffer,nOutBufferSize);
			 
	return 0;
}

class Node
{
	public:
		Node* next;
		int x;
		int y;
		int gScore;
		int hScore;
		int fScore;
};

Class NodeSet
{
	public: 
		Node* 
		bool insert;
		int size;
		
}

int FindPath(const int nStartX, const int nStartY,
			 const int nTargetX, const int nTargetY,
			 const unsigned char* pMap, const int nMapWidth, const int nMapHeight,
			 int* pOutBuffer, const int nOutBufferSize)
{
	Node *start = new Node;
	start->gScore = 0;
	start->x = nStartX;
	start->y = nStartY;
	Node *goal = new Node;
	goal->x = nTargetX;
	goal->y = nTargetY;
	start->fScore = start->gScore + (abs(start->x - goal->x) + abs(start->y - goal->y));
	set<int> ClosedSet;
	set<int> OpenSet;
	// OpenSet.insert((start->x,start->y,start->fScore));
	OpenSet.insert(&start);
	
	while (!OpenSet.empty())
	{
		findF(OpenSet,start);
	}
	// int from = ClosedSet;
	// int score = 0;
	// cur->value = (nStartY * nMapWidth) + nStartX;
	// for (int i = 0; i < nMapWidth; i++)
	// {
		// for (int j = 0; j < nMapHeight; j++)
		// {
			// if(pMap[cur->value + nMapWidth] = 1)
		// }
	// }
}

Node* findF(set<int> os, Node* start)
{
		int sml = start->fScore;
		Node *ret = start;
		// for(set<int>::iterator it = os.begin();it != os.end();it++)
		// for(int i = 0; i < os.size(); io)
		set<int>::iterator it = os.begin();
		// while(it != os.end())
		// {
			// int n = os[it->fScore];
			// if(n < sml)
			// {
				// sml = n;
				// ret = os[];
			// }
		// }
		return ret;
}

int theWork(int x, int y)
{
	
}