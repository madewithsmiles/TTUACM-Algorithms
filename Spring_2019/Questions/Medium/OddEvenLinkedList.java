/**
 *
 * @author Drew Mitchell, Texas Tech University ACM
 *
 * Problem Location: https://leetcode.com/problems/odd-even-linked-list
 *
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class OddEvenLinkedList {
    public ListNode oddEvenList(ListNode head) {
        ListNode headEven = null, headOdd = null, headOCur = null, headECur = null;
        for(int i = 1; head != null; i++) {
            if(i % 2 == 0) {
                if(headEven == null) {
                    headEven = new ListNode(head.val);
                    headECur = headEven;
                }
                else {
                    headECur.next = new ListNode(head.val);
                    headECur = headECur.next;
                }
            }
            else if(i % 2 == 1) {
                if(headOdd == null) {
                    headOdd = new ListNode(head.val);
                    headOCur = headOdd;
                }
                else {
                    headOCur.next = new ListNode(head.val);
                    headOCur = headOCur.next;
                }
            }
            head = head.next;
            if(head == null) headOCur.next = headEven;
        }
        return headOdd;
    }
}