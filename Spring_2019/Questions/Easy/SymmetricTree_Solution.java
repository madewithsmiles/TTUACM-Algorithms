/**
 * Solution by Rajeev Goonie
 *
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {

    /**
     * This is the high-level funtion that will called.
     */
    public boolean isSymmetric(TreeNode root) {
        return isSymmetric(root, root);
    }


    /**
     * How this works...
     *
     * given: root of the left and right subtrees (nodes) of a given binary tree
     *
     * if either of the nodes are null, you have two choices:
     *      1) if their both null, you still have symmetry
     *      2) else, you don't have symmetry
     *
     * otherwise, you check three conditions to check,
     *      1) the value of both nodes are the same,
     *      2) the outer nodes of the two nodes are the same (left of left checked with right of right)
     *      3) the inner nodes of the two nodes are the same (right of left checked with left of right)
     */
    private boolean isSymmetric(TreeNode leftCheck, TreeNode rightCheck){
        if(leftCheck == null || rightCheck == null){
            if(leftCheck == rightCheck)
                return true;
            return false;
        }

        boolean checkAll = (leftCheck.val == rightCheck.val) &&
                           isSymmetric(leftCheck.left, rightCheck.right) &&
                           isSymmetric(leftCheck.right, rightCheck.left);

        return checkAll;

    }

}
